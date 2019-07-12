# -*- coding: utf-8 -*-

from aqt import mw
from aqt.utils import showWarning
from anki.hooks import addHook

def getConfig():
  return mw.addonManager.getConfig(__name__)

def _subAliases(editor):
  aliases = getConfig()["aliases"]

  alias = editor.note.fields[editor.currentField]

  if alias not in aliases:
    showWarning("Bad alias \"%s\". It doesn't have a replacement rule." % alias)
  else:
    cmd = '$("#f%s").html("%s")' % (editor.currentField, aliases[alias])
    editor.web.eval(cmd)

def subAliases(editor):
  editor.saveNow(lambda: _subAliases(editor), keepFocus=True)

def setupButton(buttons, editor):
  shortcut = getConfig()["shortcut"]

  button = editor.addButton(
    None,
    "subAliases",
    subAliases,
    "Substitute aliases (%s)" % shortcut,
    "Aliases",
    keys=shortcut
  )
  return buttons + [button]

addHook("setupEditorButtons", setupButton)
