from krita import *
app = Krita.instance()
doc = app.activeDocument()

infoFill = InfoObject()
infoFill.setProperty("color", "#1f97d9")
select = Selection()
select.select(0, 0, doc.width(), doc.height(), 255)

fill = doc.createFillLayer("Non-Photo Blue", "color", infoFill, select)
root = doc.rootNode()
child = root.childNodes()

#####

# Still need a check if "Non-Photo Blue" exists, if yes -> delete the old one. Or keep it and move it, whatever is easier. 
# Any maybe an iterative name for new "Ink" layers would be great.

#####

root.addChildNode(fill, child[0])

# create Fill Layer: Non-Photo Blue
layerBlueFill = doc.nodeByName("Non-Photo Blue")
layerBlueFill.setBlendingMode("screen")

# create Paint Layer: Ink
paint = doc.createNode("Ink", "paintlayer")
root.addChildNode(paint, doc.nodeByName("Non-Photo Blue"))

doc.refreshProjection()
