from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """游戏话题详情"""

    def setUp(self):
        self.url = url + "/game/topic-detail"

    def test_1(self):
        datas['gameId'] = get_gameId()
        datas['topicId'] = get_topicId()
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
