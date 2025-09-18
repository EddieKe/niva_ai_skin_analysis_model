export const UploadImage = (imageSrc, navigate) => {
  const data = new FormData();
  data.append("file", imageSrc);
  console.log(data.get("file"));
  fetch("upload", {
    method: "put",
    body: data,
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.error) {
        console.log("Please add a photograph");
      } else {
        navigate("/recs", { state: { data } });
        console.log(data);
      }
    })
    .catch((err) => {
      console.log(err.message);
    });
};


