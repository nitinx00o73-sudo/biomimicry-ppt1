# Unity version — Game Design 1

This folder contains the gameplay controller for a Unity 3D version of the apartment game.

## Recommended setup
Unity 6.x, URP, Input System, Cinemachine.

## Scene workflow
1. Run `blender/apartment_generator.py` in Blender to create the base apartment and export FBX/GLB assets.
2. Create a Unity URP project.
3. Import the generated assets.
4. Add a first-person controller and assign Player, SecurityBot, Exit and 3 key transforms to `ApartmentGame`.
5. Add baked lighting, reflection probes, PBR materials, audio and post-processing.
