/**********************************************************************
Copyright (c) 2016 Advanced Micro Devices, Inc. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
********************************************************************/
#pragma once

#include "RadeonProRender.h"

#include <string>

//base wrap class of Baikal scene nodes
class RPR_API_ENTRY WrapObject
{
public:
    WrapObject() = default;
    virtual ~WrapObject() = default;

    template <typename T>
    static T* Cast(void* obj)
    {
        WrapObject* base = static_cast<WrapObject*>(obj);
        return dynamic_cast<T*>(base);
    };

    //name
    std::string GetName() { return m_name; }
    void SetName(const std::string& name) { m_name = name; }

    WrapObject(WrapObject&&) = default;
    WrapObject& operator= (WrapObject&&) = default;

private:
    std::string m_name;
};
