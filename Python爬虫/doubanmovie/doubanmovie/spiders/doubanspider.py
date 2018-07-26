# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    """
    爬取豆瓣电影TOP250
    """
    name = 'douban'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        """
        解析response中的字段，传送到items中
        """
        item = doubanmovie()
        movies = response.css("ol.grid_view li")
        for movie in movies:
            # 排名
            item['ranking'] = movie.css("div.pic em::text").extract_first()
            # 电影名字
            item['movie_name'] = movie.css("div.hd a span:first-child::text").extract_first()
            # 得分
            item['score'] = movie.css("div.star span.rating_num::text").extract_first()
            # 评论人数
            item['people_num'] = movie.css("div.star span:last-child::text").re("\d+")[0]
            yield item
