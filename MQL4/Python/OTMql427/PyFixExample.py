# -*-mode: python; py-indent-offset: 4; indent-tabs-mode: nil; encoding: utf-8-dos; coding: utf-8 -*-

# This code is taken from
# https://github.com/dmitryme/fix_parser/

import sys, os
from fix_fields import *
from fix_parser import *

import OTMql427
pDir = os.path.dirname(OTMql427.__file__)
pFile = b"fix.4.4.xml"
if pDir:
    pDir = os.path.join(os.path.dirname(pDir), 'etc', 'fix_descr')
    assert os.path.isdir(pDir), \
        "Installation error: cannot find the directory " +pDir
    pFile = os.path.join(bytes(pDir), pFile)
    
p = FixParser(pFile, PARSER_FLAG_CHECK_ALL)
del pDir, pFile, OTMql427

print("PROT VERSION = {0}".format(p.getProtocolVer()))
# create Exec Report
m = p.createMsg("8")
# check its params
print("MSG TYPE = {0}".format(m.getType()))
print("MSG NAME = {0}".format(m.getName()))

# fill message
m.setFieldAsString(FIXFieldTag_SenderCompID, b"QWERTY_12345678")
m.setFieldAsString(FIXFieldTag_TargetCompID, b"ABCQWE_XYZ")
m.setFieldAsInt32(FIXFieldTag_MsgSeqNum, 34)
m.setFieldAsString(FIXFieldTag_TargetSubID, "bsrv-ivanov_ii1")
m.setFieldAsString(FIXFieldTag_SendingTime, b"20120716-06:00:16.230")
m.setFieldAsString(FIXFieldTag_OrderID, b"1")
m.setFieldAsString(FIXFieldTag_ClOrdID, b"CL_ORD_ID_1234567")
m.setFieldAsString(FIXFieldTag_ExecID, b"FE_1_9494_1")
m.setFieldAsChar(FIXFieldTag_ExecType, b"0")
m.setFieldAsChar(FIXFieldTag_OrdStatus, b"1")
m.setFieldAsString(FIXFieldTag_Account, b"ZUM")
m.setFieldAsString(FIXFieldTag_Symbol, b"RTS-12.12")
m.setFieldAsChar(FIXFieldTag_Side, b"1")
m.setFieldAsDouble(FIXFieldTag_OrderQty, 25.0)
m.setFieldAsDouble(FIXFieldTag_Price, 135155.0)
m.setFieldAsChar(FIXFieldTag_TimeInForce, b"0")
m.setFieldAsDouble(FIXFieldTag_LastQty, 0)
m.setFieldAsDouble(FIXFieldTag_LastPx, 0)
m.setFieldAsDouble(FIXFieldTag_LeavesQty, 25.0)
m.setFieldAsDouble(FIXFieldTag_CumQty, 0)
m.setFieldAsDouble(FIXFieldTag_AvgPx, 0)
m.setFieldAsChar(FIXFieldTag_HandlInst, b"1")
m.setFieldAsString(FIXFieldTag_Text, b"COMMENT12")

# convert msg to string, \1 delimiter replaced with '|', just for pretty printing. '|' code is 124
str = m.toString(124)
print("MSG = {0}".format(str))

# parse input string and create FIX message
m1 = p.parse(str, 124)

# just print several fields of m1, to make sure str parsed ok
print("MSG1 TYPE = {0}".format(m1.getType()))
print("MSG1 NAME = {0}".format(m1.getName()))
print("SenderCompID = {0}".format(m1.getFieldAsString(FIXFieldTag_SenderCompID)))
print("TargetCompID = {0}".format(m1.getFieldAsString(FIXFieldTag_TargetCompID)))
