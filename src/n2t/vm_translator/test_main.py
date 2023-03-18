import unittest
from n2t.vm_translator.main import Main


class TestMain(unittest.TestCase):
    def test_translator(self):
        vm_file = '/Users/wupeng/projects/nand2tetris/src/hdl/07/MemoryAccess/BasicTest/BasicTest.vm'

        main = Main(vm_file)
        main.run()
        expected_out_file = '/Users/wupeng/projects/nand2tetris/src/hdl/07/MemoryAccess/BasicTest/BasicTest.asm'
        with open(expected_out_file, 'r') as f:
            for line in f:
                print(line)


if __name__ == '__main__':
    unittest.main()
