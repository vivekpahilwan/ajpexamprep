class Animal:
    def make_sound(self):
        return "Unknown sound"

    def make_sound(self, sound):
        return f"Animal makes {sound} sound"

    def make_sound(self, sound, volume):
        return f"Animal makes {sound} sound at volume {volume}"

a = Animal()
               # Output: Unknown sound
       # Output: Animal makes roar sound
print(a.make_sound("loud")) # Output: Animal makes meow sound at volume loud
