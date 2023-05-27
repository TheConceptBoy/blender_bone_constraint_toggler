# blender_constraint_toggler
 A simple plugin that adds a couple of menu options to enable or disables all bone constraints on any selected armatures.
 
 ![image](https://github.com/TheConceptBoy/blender_bone_constraint_toggler/assets/52581279/081a3142-27e7-45e4-ab0c-f36ec6eec1b0)
 
 **Problem** 
 When exporting rigged characters from blender to be used in your game engine, you must remeber that all bone constraints need to be disabled. Otherwise your exporeted animations will be mangled. 

**Dumb Workarounds**

(Option A) Make a copy of your armature, which is rigged with all your IK and Constraint goodies, which you actually use to animate and then  either retarget the bone data into your clean armature to which your character mesh is attached, or remember to copy the baked animations from the IK rig to the clean rig every time.

(Option B) Manually go through all bones within your rig  every time you need to export and disable every single constraint by hand so you can export just you baked animations. Seriously, I don't understand why the export option doesn't already have this in place. Oh and don't forget to now painstaikingly re-enable all of them one at a time if you want to add some more animations.


Seriosuly... thousands of animators using Blender and nobody thought of this being an issue? 
 
 
 **(Option C)**
 blender_bone_constraint_toggler plugin - Saves you time by having you not need a second armature to which you copy your animations every time or having to painstakingly cycle through each bone and disable each bone constraint one at a time.
 For cases when making video game character animations and you need to export your rigged and animated mesh in formats like GLTF which, will get messed up if you forget to disable your constraints.
 
 This should really be an export option and it shoul've have been stock feature of Blender about 10 years ago.
 
 

