#!/usr/bin/env python
# Code original from Lua Love
import sys
import os
import plistlib
import json

luaSyntax = os.path.join('..', '..', 'Lua', 'Lua.tmLanguage')
syntaxOutput = os.path.join('..', 'CoronaSDK.tmLanguage')
completionsOutput = os.path.join('..', 'CoronaSDK.sublime-completions')

name = 'Lua (CoronaSDK)'
comment = 'Lua+CoronaSDK Syntax'
scopeName = 'source.lua'
uuid = '93E017CC-6F27-11D9-90EB-000D93589AF7'
syntaxGroup = 'support.function.library.lua'

def tmize(node):
    assert(isinstance(node, dict))
    buf = []
    for key, val in node.items():
        if len(val.keys()) == 0:
            buf.append(key)
        else:
            buf.append('%s\.%s' % (key, tmize(val)))
    return '(%s)' % '|'.join(buf)
 
def main():
    # Parse api
    theFile = open('api.txt')
    apiList = [line.strip() for line in theFile.read().split() if line]
    theFile.close()

    # Build api hierarchy
    apiDict = {}
    for line in apiList:
        namespace = apiDict
        for token in line.split('.'):
            if not namespace.get(token):
                namespace[token] = {}
            namespace = namespace[token]
    # Clone lua syntax and insert metadata
    plist = plistlib.readPlist(luaSyntax)
    plist['name'] = name
    plist['scopeName'] = scopeName
    plist['comment'] = comment
    plist['uuid'] = uuid

    # Insert CoronaSDK API
    coronaDict = {
        'name': syntaxGroup,
        'match': r'(?<![^.]\.|:)\b%s\b(?=[( {])' % tmize(apiDict)
    }
    plist['patterns'].append(coronaDict)
    plistlib.writePlist(plist, syntaxOutput)
    print ' --> Created %s' % syntaxOutput

    # Build completions file

    completions = []
    for line in apiList:
        completions.append({
            'trigger': line,
            'contents': '%s($0)' % line,
        })
    theFile = open(completionsOutput, 'w')
    json.dump({
        'scope': scopeName,
        'completions': completions,
    }, theFile, sort_keys=True, indent=4)
    theFile.close()
    print ' --> Created %s' % completionsOutput

if __name__ == '__main__':
    if len(sys.argv) > 1:
        luaSyntax = sys.argv[1]

    if not os.path.exists(luaSyntax):
        print ' --> Lua.tmLanguage not found.'
        sys.exit(1)

    main()
