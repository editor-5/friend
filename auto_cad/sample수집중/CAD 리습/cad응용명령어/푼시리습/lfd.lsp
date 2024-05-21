(defun C:LayerFiltersDelete ()
(vl-Load-Com)
(vl-Catch-All-Apply
'(lambda ()
(vla-Remove (vla-GetExtensionDictionary
(vla-Get-Layers 
(vla-Get-ActiveDocument
(vlax-Get-Acad-Object))))
"ACAD_LAYERFILTERS")))
(princ "\nAll layer filters have been deleted.")
(princ))
(defun C:LFD () (C:LayerFiltersDelete))
