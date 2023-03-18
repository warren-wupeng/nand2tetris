
class Main:

    def __init__(self, vm_file):
        self.vm_file = vm_file
        self.asm_file = vm_file.replace('.vm', '.asm')

    def run(self):
        with open(self.asm_file, 'w') as f:
            f.write('// translated')
