Attribute VB_Name = "Module1"
Sub Shuffle_slides()
FirstSlide = 2
lastslide = ActivePresentation.Slides.Count

Randomize
For i = FirstSlide To lastslide
RSN = Int((lastslide - FirstSlide + 1) * Rnd + FirstSlide)
ActivePresentation.Slides(i).MoveTo (RSN)
Next i


End Sub
