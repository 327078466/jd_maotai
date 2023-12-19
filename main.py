#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

import log
from jd_assistant import Assistant

if __name__ == '__main__':
    # sku_ids = '100066167064'  # 商品id
    sku_ids = '100030659205'  # 商品id
    # sku_ids = '10085429975102'  # 商品id
    area = '12_904_3373_62096'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    while 1:
         mode = input("1-普通商品(先加购物车再提交订单) 2-预约商品(可加购物车) 3-预约商品(不可加购物车) 4-预售商品(支付定金) 5-退出 Enter mode: ")
         # 库存监控模式
         if mode == '1':
            # 6个参数：
            # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
            # area: 地区id
            # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
            # stock_interval: 查询库存时间间隔，可选参数，默认3秒
            # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
            # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
            asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
         # 预约可加入购物车模式
         elif mode == '2':
            type = input("Enter type: 1-立即预约 2-立即抢购")
            buy_time= '2023-11-29 12:00:00.000'
            # 6个参数：
            # sku_id: 商品id
            # buy_time: 购买时间
            # stock_interval: 查询库存时间间隔，可选参数，默认3秒
            # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
            # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
            if type == '1':
                asst.appoint_sku(sku_ids)
                print("\n")
                # asst.appoint_sku(sku_ids)
            else:
                asst.exec_reserve_seckill_by_time(sku_ids,buy_time)
         # 预约抢购模式
         elif mode == '3':
             type = input("Enter type: 1-立即预约 2-立即抢购")
             buy_time= '2023-11-29 12:00:00.000'
             # 6个参数：
             # sku_id: 商品id
             # buy_time: 购买时间
             # stock_interval: 查询库存时间间隔，可选参数，默认3秒
             # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
             # submit_interval: 提3交订单失败后重试时间间隔，可选参数，默认5秒
             if type == '1':
                 asst.appoint_sku(sku_ids)
                 print("\n")
             else:
                 asst.exec_seckill_by_time(sku_ids=sku_ids,buy_time=buy_time)
                 print("\n")
         # 预售模式
         elif mode == '4':
             # 定金url https://yuding.jd.com/presaleInfo/getPresaleInfo.action?callback=yushouNoWayJDCB&sku=100025256835
             #   {"overseaPurchaseCookies":"","vendorRemarks":"[]","submitOrderParam.sopNotPutInvoice":"false","submitOrderParam.presaleMobile":"188****7110","submitOrderParam.presalePayType":"2","submitOrderParam.trackID":"TestTrackId","flowType":"15","preSalePaymentTypeInOptional":"2","submitOrderParam.ignorePriceChange":"0","submitOrderParam.btSupport":"0","submitOrderParam.payType4YuShou":"2","submitOrderParam.eid":"jdd0353F3RSGW6RX5IHYYDZIDMYHMR7BOEHLXQVR3F4BNY3UZET7B2OA36SHYEEVEGEBE6RTAZ4OEKI7HDUWQ4ILCHXCTIIAAAAMMDI3MRWAAAAAACJRK5DNRRRG5DAX","submitOrderParam.fp":"b6269b7f2de05621d407e0ab1e2a315c","submitOrderParam.preMainSkuId":"100025256835","submitOrderParam.jxj":"1","submitOrderParam.zpjd":"1","submitOrderParam.giftRemove":"0","submitOrderParam.limitUserFlag":"67776"}
             print("在开发中~")
             continue
         elif mode == '5':
             sys.exit(0)
         else:
             print("输入参数有误请重新输入~")
             continue
