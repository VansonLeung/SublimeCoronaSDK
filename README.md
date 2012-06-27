Description
===========

This is work in progress and managed in my free time, I will uppdate the completions, API and code etc when I have some time to spare. Many hours have been spent on making this so enjoy....

-- Known issues --
If you type; display and choose from the completions list the insertions works fine but if you type; display.new...... then it becomes display.display.newImageRect()

Feel free to fix it.


-- Installation --

Add the entire SublimeCoronaSDK folder to the Packages folder.

-- Usage --
Just type and you'll get available completions in the little popUp, continue to type and ST2 will match the best ones. flick through the list with arrow keys or scroll with mouse to the API you want. Hit Enter or Tab key.

-- Build -- 
To use the build command, hit cmd+B to run program. The build command only works if you're file is in the same directory as main.lua so files in subdirectories does not launch the Corona simulator.

-- Warning! -- 
Not actually a warning but if you have a buch of snippets installed then they will also show up in the completions popUP. if you find that irritating then just remove the snippets.

-- Other things added --
I've added most of the libraries built into corona and some other such as director, lime, ui, movieclip etc...
so when start typing: require you'll get the list of the libraries. Important is that you need to add 3:rd party libs yourself to your project or it'll give you errors.

-- Good to Know -- 
When you use widgets you'll see you can either use a widget with () or {}. In the first case () you need to add a optionsTable. In the other case {} some of the data is already written for you, if you need other params then you can just add or change them.

-- Comming sometime later --
Sometime later I'll add pre-filled optionsTables for each widget, they'll be named sliderOptions = {}, buttonOptions = {}, tabBarOptions = {}, scrollViewOptions = {}, pickerWheelOptions = {}, tableViewOptions = {} etc....

There's also basic tables for smsOptions = {}, mailOptions = {} and inApp purchase products productsTable = {}.

Updated with the new improved sprite API. For newImageSheet, type sheetOptions to get the sheetOptions = {}.

All known Public Corona Api are added.







