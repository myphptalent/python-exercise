#Demostrate the template string function

from string import Template

def main():
    # Usual string formating with format()
    str1 = "You are watching {0} by {1}".format("Advanced Python", "Joi")
    print(str1)

    #TODO: Create a template with placeholder
    templ = Template("You are watching ${title} by ${author}")
    
    #TODO: Use the substitution method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Joi") 
    print(str2)

    #TODO: Use the substitute method with a dictionary
    data = {
        "author" : "Joe",
        "title"   : "Advanced Python"
    }

    str3 = templ.substitute(data)
    print(str3)




if __name__ =="__main__":
    main()