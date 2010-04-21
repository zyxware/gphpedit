/* This file is part of gPHPEdit, a GNOME2 PHP Editor.
 
   Copyright (C) 2003, 2004, 2005 Andy Jeffries <andy at gphpedit.org>
   Copyright (C) 2009 Anoop John <anoop dot john at zyxware.com>
	  
   For more information or to find the latest release, visit our 
   website at http://www.gphpedit.org/
 
   gPHPEdit is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   gPHPEdit is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with gPHPEdit.  If not, see <http://www.gnu.org/licenses/>.
 
   The GNU General Public License is contained in the file COPYING.
*/
#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#ifndef MAIN_H
#define MAIN_H

#include <glib.h>
#include <gtk/gtk.h>
#include <gdk/gdkkeysyms.h>
#include <gtkscintilla.h>

#ifdef ENABLE_NLS
#include <glib/gi18n.h>
#else							/* ENABLE_NLS */
#define _(String)(String)
#define N_(String)(String)
#endif							/* ENABLE_NLS */

#define GPHPEDIT_PIXMAP_ICON "gphpedit.png"
#define GPHPEDIT_PIXMAP_FULL_PATH (PIXMAP_DIR "/" GPHPEDIT_PIXMAP_ICON)
gint debug(gchar *strMsg, ...);
#endif
