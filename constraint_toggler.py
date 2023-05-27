bl_info = {
	"name": "Bone Constraint Toggler",
	"blender": (2, 80, 0),
	"category": "Object",
}

import bpy

class ArmatureConstraintsToggleMenu(bpy.types.Menu):
	bl_idname = "OBJECT_MT_custom_menu"   	# Unique identifier for buttons and menu items to reference.
	bl_label = "Bone Constraint Toggler"		 # Display name in the interface.
	bl_icon = "CONSTRAINT_BONE"
	
	def draw(self, context):
		layout = self.layout
		#layout.label(text="En/Dis All Selected armature Bone Constraints")
		layout.operator(DisableArmatureConstraints.bl_idname, text="Mute All Bone Constraints", icon='HIDE_ON')
		layout.operator(EnableArmatureConstraints.bl_idname, text="Unmute All Bone Constraints", icon='HIDE_OFF')

		# call the second custom menu
	#	layout.menu("OBJECT_MT_sub_menu", icon="COLLAPSEMENU")
		

class EnableArmatureConstraints(bpy.types.Operator):
	"""Enable / Disable All constraints within bones any selected armatures"""      # Use this as a tooltip for menu items and buttons.
	bl_idname = "object.enable_armature_constraints"		# Unique identifier for buttons and menu items to reference.
	bl_label = "Enable Armature Constraints"		 # Display name in the interface.
	bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

	def execute(self, context): 	   # execute() is called when running the operator.

		print(context.scene.objects)
		constraint_count = 0
		armature_found = False
		constraint_found = False
		for obj in context.selected_objects:

		
			if obj.type == "ARMATURE":
				print("this is an armature")
				armature_found = True
				
				print(obj.pose.bones)
				
				
				for bone in obj.pose.bones:
					print(bone.constraints)
					
					
					for con in bone.constraints:
						constraint_found = True
						if con.enabled == False:
							constraint_count += 1
							con.enabled = True
		
		if armature_found == False:
			self.report({'WARNING'}, 'No Armatures Selected')	
		elif constraint_found:
			self.report({'INFO'}, str(constraint_count) + ' Bone Constraints Enabled')				
		else:
			self.report({'WARNING'}, 'No Constraints found.')
					
					
		return{'FINISHED'}  

				
class DisableArmatureConstraints(bpy.types.Operator):
	"""My Object Moving Script"""      # Use this as a tooltip for menu items and buttons.
	bl_idname = "object.disable_armature_constraints"   	 # Unique identifier for buttons and menu items to reference.
	bl_label = "Disable Armature Constraints"   	  # Display name in the interface.
	bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

	def execute(self, context): 	   # execute() is called when running the operator.
		constraint_count = 0
		constraint_found = False
		armature_found = False
		
		for obj in context.selected_objects:
			if obj.type == "ARMATURE":
				armature_found = True
				
				for bone in obj.pose.bones:
					print(bone.constraints)
					
					for con in bone.constraints:
						constraint_found = True
						if con.enabled == True:
							constraint_count += 1
							con.enabled = False
			
		if armature_found == False:
			self.report({'WARNING'}, 'No Armatures Selected')	
		elif constraint_found:
			self.report({'INFO'}, str(constraint_count) + ' Bone Constraints Disabled')				
		else:
			self.report({'WARNING'}, 'No Constraints found.')
				  
		return {'FINISHED'} 		   # Lets Blender know the operator finished successfully.

def menu_func_enable(self, context):
	self.layout.menu(ArmatureConstraintsToggleMenu.bl_idname, icon="CONSTRAINT_BONE")
	


def register():
	#menu for this tool
	bpy.utils.register_class(ArmatureConstraintsToggleMenu)
	bpy.types.VIEW3D_MT_object.append(menu_func_enable)  # Adds the new operator to an existing menu.

	bpy.utils.register_class(EnableArmatureConstraints)
	bpy.utils.register_class(DisableArmatureConstraints)

def unregister():
	bpy.utils.unregister_class(ArmatureConstraintsToggleMenu)
	
	bpy.utils.unregister_class(EnableArmatureConstraints)
	bpy.utils.unregister_class(DisableArmatureConstraints)




# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
	register()