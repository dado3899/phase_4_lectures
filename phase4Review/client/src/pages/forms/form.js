import { Formik, Form, Field, ErrorMessage } from "formik";
export default function form({loggedIn}) {
    console.log(loggedIn)
    
    return(
    <div>
        <Formik 
        initialValues={{ email: '', fullname: '' }}
        onSubmit={(formData) => {
            console.log(formData);
        }}>
            <Form>
                <Field
                type="text"
                name="fullname"
                placeholder="Enter your fullname"
                />
                <Field
                type="email"
                name="email"
                placeholder="Enter email address"
                />
                <Field type="password" name="password" />
                <button type="submit">
                Submit
                </button>
            </Form>
        </Formik>
    </div>
    )
    
}

    