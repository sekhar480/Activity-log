// UdpSampDLL.h : main header file for the UDPSAMPDLL DLL
//

#if !defined(AFX_UDPSAMPDLL_H__13A37F6B_9B77_4C67_B03C_A97246076681__INCLUDED_)
#define AFX_UDPSAMPDLL_H__13A37F6B_9B77_4C67_B03C_A97246076681__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CUdpSampDLLApp
// See UdpSampDLL.cpp for the implementation of this class
//

class CUdpSampDLLApp : public CWinApp
{
public:
	CUdpSampDLLApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CUdpSampDLLApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

	//{{AFX_MSG(CUdpSampDLLApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_UDPSAMPDLL_H__13A37F6B_9B77_4C67_B03C_A97246076681__INCLUDED_)
