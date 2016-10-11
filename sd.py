# Web.py
import web
from web import form

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form( 
    form.Textbox("Name"),
	
    form.Textbox("Branch"), 
    form.Textbox("Cpi", 
        form.notnull,
        
        form.Validator('Must be number less than 10', lambda x:float(x)<=10)),
    form.Textarea('Skill'),
    form.Checkbox('I agree'), 
    form.Dropdown('Hostel', ['Kapili', 'Dihing', 'Barak','Umiyam','siang'])) 

class index: 
    def GET(self): 
        form = myform()
        
        return render.san(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.san(form)
        else:
   
            return " Hello You are successfully registered. \n       Name: %s, Branch: %s" % (form.d.Name, form['Branch'].value)

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
