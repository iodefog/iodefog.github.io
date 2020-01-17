#! /usr/local/bin/python 
# -*- coding: cp936 -*-

# @desc python通过BT种子生成磁力链接  
# @date 2015/11/10 
# @author pythontab.com 
import bencode 
import sys 
import hashlib 
import base64 
import urllib 
#获取参数 
torrentName = sys.argv[1] 
#读取种子文件 
torrent = open(torrentName, 'rb').read() 
#计算meta数据 
metadata = bencode.bdecode(torrent) 
hashcontents = bencode.bencode(metadata['info']) 
digest = hashlib.sha1(hashcontents).digest() 
b32hash = base64.b32encode(digest) 
#打印 
print 'magnet:?xt=urn:btih:%s' % b32hash