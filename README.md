# Creation Kit DialogueView fixer
Why?
If new master added to esp, dialogueview form ids are changed, this breaks your pretty dialogue view.
This tool fixes broken dialogueview if masters added/removed to esp.
Automatization of [this](https://www.reddit.com/r/skyrimmods/comments/cq3a74/protip_fixing_dialog_views_after_adding/) process

# Usage:
1. Then esp masters amount changed, count them and convert decimal count into haxadecimal (10 -> 0a, 32 -> 20)
2. Run script with one argument of new count in hex from any location:
    ```
    python(3) dilogueview_fixer.py [new masters count in hex]
    ```
3. Chose folder with your dialogue view files.
4. Wait until it finished working.

# Attention
This script provided as-is.
This scripts will process ALL files in folder, so make sure your mod is stored in a dedicated folder.
Although it will not delete any files, just create new ones near old, old files might be deleted.
CHECK IF EVERYTHING ALRIGHT BEFORE DELETING ANYTHING.
