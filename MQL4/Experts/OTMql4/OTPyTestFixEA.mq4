// -*-mode: c; c-style: stroustrup; c-basic-offset: 4; coding: utf-8-dos -*-

#property copyright "Copyright 2015 OpenTrading"
#property link      "https://github.com/OpenTrading/"
#property strict

#define INDICATOR_NAME          "PyTestFixEA"

#include <OTMql4/OTLibLog.mqh>
#include <OTMql4/OTPy27.mqh>

#include <WinUser32.mqh>
void vPanic(string uReason) {
    "A panic prints an error message and then aborts";
    vError("PANIC: " + uReason);
    MessageBox(uReason, "PANIC!", MB_OK|MB_ICONEXCLAMATION);
    // I dont think ExpertRemove actually removes the expert
    ExpertRemove();
}

extern string sStdOutFile="../../Logs/_test_PyTestFixEA.txt";

int OnInit() {
    int iRetval;
    string uArg, uRetval;

    iRetval = iPyInit(sStdOutFile);
    if (iRetval != 0) {
        return(iRetval);
    }
    Print("Called iPyInit");
    
    uArg="import sys, os";
    vPyExecuteUnicode(uArg);
    // VERY IMPORTANT: if the import failed we MUST PANIC
    vPyExecuteUnicode("sFoobar = '%s : %s' % (sys.last_type, sys.last_value,)");
    uRetval=uPyEvalUnicode("sFoobar");
    if (StringFind(uRetval, "exceptions.SystemError", 0) >= 0) {
        // Were seeing this during testing after an uninit 2 reload
        uRetval = "PANIC: import sys,os failed - we MUST restart Mt4:"  + uRetval;
        vPanic(uRetval);
        return(-2);
    }
        
    /* sys.path is too long to fit a log line */
    uArg="str(sys.path[0:1])";
    uRetval = uPySafeEval(uArg);
    if (StringFind(uRetval, "ERROR:", 0) >= 0) {
	uRetval = "ERROR: sys.path failed: "  + uRetval;
	vWarn("OnInit: " +uRetval);
	// return;
    } else {
	Print("sys.path = "+uRetval);
    }
    
    vPyExecuteUnicode("print('os.getpid() == %d' % os.getpid())");
    iRetval = iPyEvalInt("os.getpid()");
    Print("os.getpid() = " + iRetval);
    
    uArg="from OTMql427 import PyFixExample";
    vPyExecuteUnicode(uArg);
    uArg="str(dir(PyFixExample))";
    uRetval = uPySafeEval(uArg);
    Print("dir(PyFixExample) = " + uRetval);
    vPyExecuteUnicode("sys.stderr.flush()");
    return (0);
}
int iTick=0;

void OnTick () {
    iTick+=1;
    // Print("iTick="+iTick);
}

void OnDeinit(const int iReason) {
    //? if (iReason == INIT_FAILED) { return ; }
    vPyDeInit();
}
