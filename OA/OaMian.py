#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Seeyou import Seeyou
from OA.Weaver import Weaver
from OA.Ruvar import Ruvar
from OA.Tongda import Tongda
def Main(ThreadPool,Url,Values,UnixTimestamp):
    Seeyou.Main(ThreadPool,Url,Values,UnixTimestamp)
    Weaver.Main(ThreadPool, Url, Values, UnixTimestamp)
    Ruvar.Main(ThreadPool, Url, Values, UnixTimestamp)
    Tongda.Main(ThreadPool, Url, Values, UnixTimestamp)