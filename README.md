基本思路：8.26

1. 用mongodb存储股票代码，然后依靠mongodb的大数据查询特效遍历拿出股票代码
2. 在爬取单个股票数据时拼接url即可。
3. 为了更好的比对，最终爬取的数据都存入mysql