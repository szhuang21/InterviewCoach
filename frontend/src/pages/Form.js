import React from "react";
import { useHistory } from "react-router-dom";
import { useState } from "react";

const FormPage = () => {
  const { push } = useHistory();
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    gender: "male",
    genderPreference: "men",
    sexuality: "",
    instagram: "",
    snapchat: "",
  });

  const [formSubmitted, setFormSubmitted] = useState(false);
  const [errors, setErrors] = useState({});

  const genders = [
    { id: 1, name: "Male" },
    { id: 2, name: "Female" },
    { id: 3, name: "Nonbinary" },
  ];

  const sexualities = [
    { id: 1, name: "Straight" },
    { id: 2, name: "Gay" },
    { id: 3, name: "Lesbian" },
    { id: 4, name: "Bisexual" },
    { id: 5, name: "Other" },
  ];

  const genderPreferences = [
    // EVENTUALLY CREATE A SELECT ALL
    { id: 1, name: "Men" },
    { id: 2, name: "Women" },
    { id: 3, name: "Nonbinary people" },
    { id: 4, name: "Everyone" },
  ];

  const handleChange = (event) => {
    setFormData((prevalue) => {
      return {
        ...prevalue,
        [event.target.name]: event.target.value,
      };
    });

    // setFormData((prevalue) => {
    //   return {
    //     ...prevalue,
    //     [event.target.name]: event.target.value,
    //   };
    // });
  };

  const handleValidation = () => {
    let errors = {};
    let formIsValid = true;

    // name
    if (!formData.name) {
      formIsValid = false;
      errors["name"] = "Cannot be empty";
    }

    if (typeof formData.name !== "undefined") {
      if (!formData.name.match(/^[a-zA-Z\w\s]+$/)) {
        formIsValid = false;
        errors["name"] = "Only letters";
      }
    }

    //Email
    if (formData.email) {
      formIsValid = false;
      errors["email"] = "Cannot be empty";
    }

    if (typeof formData.email !== "undefined") {
      let lastAtPos = formData.email.lastIndexOf("@");
      let lastDotPos = formData.email.lastIndexOf(".");

      if (
        !(
          lastAtPos < lastDotPos &&
          lastAtPos > 0 &&
          formData.email.indexOf("@@") == -1 &&
          lastDotPos > 2 &&
          formData.email.length - lastDotPos > 2
        )
      ) {
        formIsValid = false;
        errors["email"] = "Email is not valid";
      }

      if (
        formData.email.substring(lastAtPos, formData.email.length) !==
        "@illinios.edu"
      ) {
        formIsValid = false;
        errors["email"] = "Not an illinois.edu email";
      }
    }

    // social media
    if (typeof formData.instagram !== "undefined") {
      if (!formData.instagram.match(/^[a-z0-9_\.]+$/)) {
        formIsValid = false;
        errors["instagram"] = "Invalid Instagram Username";
      }
    }

    if (typeof formData.snapchat !== "undefined") {
      if (!formData.snapchat.match(/^[a-z0-9_\.]+$/)) {
        formIsValid = false;
        errors["snapchat"] = "Invalid Snapchat Username";
      }
    }

    setErrors(errors);
    return formIsValid;
  };

  const handleSubmit = (event) => {
    // push({
    //   pathname: "/submitted",
    //   state: { formData }, // your data array of objects
    // });

    // push("/submitted");
    if (handleValidation()) {
      alert("Form Submitted");
    } else {
      alert("Form Has Errors");
    }

    setFormSubmitted(true);
    event.preventDefault();

    console.log("formData ", formData);
    let code = new URLSearchParams(window.location.search).get("code");

    // console.log(qs.parse(this.props.location.search, { ignoreQueryPrefix: true }).code)

    // TODO: ADD SPOTIFY OAUTH STUFF HERE

    let jsonData = {
      gender: "male",
      sexuality: "straight",
      name: formData["name"],
      preference: formData["genderPreference"],
      ig_username: "placeholder_name",
      snap_username: "placeholder_name",
      email: formData["email"],
      code: code,
    };

    fetch("http://127.0.0.1:5000/register", {
      mode: "cors",
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(jsonData),
    })
      .then(function (response) {
        console.log(response);

        if (response.status === 200) {
          push({
            pathname: "/submitted",
            state: { formData }, // your data array of objects
          });
        } else {
          console.log("An error has occurred.");
        }
      })
      .catch(function (error) {
        console.log(error);
      });

    // setFormData({
    //   // clears data
    //   name: "",
    //   email: "",
    //   genderPreference: "",
    // });
  };

  return (
    <div class="p-10 max-w-sm">
      <div class="text-xl text-black font-bold font-montserrat mb-1">
        HeartBeats 💞
      </div>
      <div class="text-xs text-gray-600 font-montserrat">
        Welcome! Please enter your details to find your HeartBeat match.
      </div>

      <div class="w-full font-montserrat">
        <form onSubmit={handleSubmit}>
          <div class="mb-4 mt-2">
            <label for="name" class="font-bold">
              Name
            </label>
            <input
              class="border rounded w-full py-2 px-3 text-xs text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="enter your full name"
              type="text"
              name="name"
              onChange={handleChange}
            />
          </div>

          <div class="mb-4">
            <label for="name" class="font-bold">
              Email
            </label>
            <input
              class="border rounded w-full py-2 px-3 text-xs text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="enter your illinois.edu email"
              type="text"
              name="email"
              onChange={handleChange}
            />
          </div>

          <div class="mb-4">
            <label for="name" class="font-bold">
              I identify as:
            </label>

            <select
              className="w-full py-2 px-3 text-xs text-gray-800 bg-white border rounded shadow-sm outline-none appearance-none"
              value={formData.genderPreference}
              label="gender"
              onChange={handleChange}
              name="gender"
            >
              {genders.map((item) => (
                <option value={item.name}>{"  " + item.name}</option>
              ))}
            </select>
          </div>

          <div class="mb-4">
            <label for="name" class="font-bold">
              I am:
            </label>

            <select
              className="w-full py-2 px-3 text-xs text-gray-800 bg-white border rounded shadow-sm outline-none appearance-none"
              value={formData.genderPreference}
              label="sexuality"
              onChange={handleChange}
              name="sexuality"
            >
              {sexualities.map((item) => (
                <option value={item.name}>{"  " + item.name}</option>
              ))}
            </select>
          </div>

          {/* I can see this question leading to troll answers if a person says they're straight but then says they're interested in men */}
          <div class="mb-4">
            <label for="name" class="font-bold">
              I'm interested in:
            </label>

            <select
              className="w-full py-2 px-3 text-xs text-gray-800 bg-white border rounded shadow-sm outline-none appearance-none"
              value={formData.genderPreference}
              label="Gender Preference"
              onChange={handleChange}
              name="genderPreference"
            >
              {genderPreferences.map((item) => (
                <option value={item.name}>{"  " + item.name}</option>
              ))}
            </select>
          </div>

          <div class="mb-4">
            <label for="name" class="font-bold">
              Instagram
            </label>
            <input
              class="border rounded w-full py-2 px-3 text-xs text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="enter your instragram handle"
              type="text"
              name="instagram"
              onChange={handleChange}
            />
          </div>

          <div class="mb-6">
            <label for="name" class="font-bold">
              Snapchat
            </label>
            <input
              class="border rounded w-full py-2 px-3 text-xs text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="enter your snapchat username"
              type="text"
              name="snapchat"
              onChange={handleChange}
            />
          </div>

          <input
            type="submit"
            value="Send It"
            class="text-white bg-zinc-900 rounded-lg w-full p-1"
            // onClick={this.onSubmit}
          />
        </form>
      </div>
    </div>
  );
};

export default FormPage;
