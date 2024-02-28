/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-05-23 23:05:27
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-05-27 18:05:42
 */

#ifndef __OS_H__
#define __OS_H__
/**
 * Determination a platform of an operation system
 * Fully supported supported only GNU GCC/G++, partially on Clang/LLVM
 */

#ifdef __cplusplus
extern "C" {
#endif

// Return a name of platform, if determined, otherwise - an empty string
const char *getOSName();

#ifdef __cplusplus
}
#endif

#endif /* __OS_H__ */
