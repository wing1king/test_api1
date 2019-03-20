from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """生成订单"""

    def setUp(self):
        self.url = url + "/pay/add-order"

    def test_1(self):
        datas['productId'] = 'com.idreamsky.avg.diamond.10'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
