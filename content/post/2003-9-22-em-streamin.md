+++
date = "2003-09-22T07:46:56+00:00"
title = "EM_STREAMIN"
+++



What do you usually do when you need to set text in a Windows control? You do
one of the following:

  * SetWindowText()
  * SetDlgItemText()
  * SendMessage(WM_SETTEXT)
  * SendMessage(WM_SETTEXTEX)

It's tempting to do the same for a Rich Edit control, and sure enough, this
will work on almost all versions of Windows.

On early '98 systems, however, it won't always work. In cases where it
doesn't, it either displays gobbledygook, does nothing, or crashes -- pretty
easy for this to slip by QA. Moreover, after looking into the MSDN
documentation on the subject, I don't actually see any guarantee that simply
setting text on a Rich Edit control will work on _any_ version of Windows.

Instead, you must stream text into these controls. Doing so is a little more
cumbersome than a single function call, but it's simple boilerplate code. Here
is an example of how to do it:

    
    
    static DWORD CALLBACK editStreamCallback(DWORD_PTR dwCookie,
                                             LPBYTE pbBuff,
                                             LONG cb,
                                             LONG *pcb)
    {
        esstruct *ess = (esstruct *)dwCookie;
        if (NULL != ess) {
            *pcb = cb;
            if (*pcb > ess->nSize) {
                *pcb = ess->nSize;
            }
            if (*pcb > 0) {
                memcpy(pbBuff, ess->lpText, *pcb);
                ess->lpText += *pcb;
                ess->nSize -= *pcb;
            }
            return 0;
        }
        return ERROR_INVALID_PARAMETER;
    }
    
    void SetTextForMyControl(LPTSTR *text)
    {
        esstruct ess;
        EDITSTREAM es;
    
        ess.lpText = text;
        ess.nSize = (text->get_Length()) * sizeof(TCHAR);
    
        es.dwCookie = (DWORD_PTR)&ess;
        es.dwError = 0;
        es.pfnCallback = editStreamCallback;
    
        SendMessage(GetDlgItem(hwnd, IDC_MYCONTROL),
            EM_STREAMIN,
            (WPARAM)(SF_TEXT /* optional: | SF_UNICODE*/),
            (LPARAM)&es);
    }

This performs extremely reliably on all Windows systems I have tested. I
strongly recommend that you use it whenever you want to set text on a Rich
Edit control.

