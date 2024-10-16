#ifndef __ANSI_COLORS_H__
#define __ANSI_COLORS_H__

#define RED_TEXT "\033[0;31m"
#define GREEN_TEXT "\033[0;32m"
#define YELLOW_TEXT "\033[0;33m"
#define BLUE_TEXT "\033[0;34m"
#define MAGENTA_TEXT "\033[0;35m"
#define CYAN_TEXT "\033[0;36m"

#define BOLD_RED_TEXT "\033[1;31m"
#define BOLD_GREEN_TEXT "\033[1;32m"
#define BOLD_YELLOW_TEXT "\033[1;33m"
#define BOLD_BLUE_TEXT "\033[1;34m"
#define BOLD_MAGENTA_TEXT "\033[1;35m"
#define BOLD_CYAN_TEXT "\033[1;36m"

#define RESET_COLOR "\033[0m"

void setupConsole(void);
void restoreConsole(void);

#endif /* __ANSI_COLORS_H__ */
