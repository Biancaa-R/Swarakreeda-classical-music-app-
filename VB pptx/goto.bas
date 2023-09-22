Attribute VB_Name = "Module1"

Sub goto_slide()
FirstSlide = 1
lastslide = ActivePresentation.Slides.Count

ActivePresentation.Slides(FirstSlide).MoveTo (lastslide)
End Sub
