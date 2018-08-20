import unittest
from freeproxy.channels.xici import XiCi
import asyncio


class Test_Xici(unittest.TestCase):
    def test_xici(self):
        coro = XiCi().batch()
        loop = asyncio.get_event_loop()
        rst = loop.run_until_complete(asyncio.ensure_future(coro))
        print(rst)


def main():
    unittest.main()


if __name__ == '__main__':

    main()
