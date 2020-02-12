import unittest

def showMsg(msg):
    return('%s'%(msg))
def do_dibide(a,b):
    return(a/b)
def showTrue(flag):
    return(flag)
class TestSomeFunc(unittest.TestCase):
    def testrun(self):
        self.assertEqual('OK',showMsg('OK'))
        self.assertNotEqual('OK',showMsg('NO'))
        self.assertTrue(do_dibide(1,2))
        self.assertIs(showTrue(False),False)
        self.assertIs(int(do_dibide(1,2)),1)

if __name__=='__main__':
    unittest.main()