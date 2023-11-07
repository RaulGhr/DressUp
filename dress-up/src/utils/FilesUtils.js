export const encodeImgToBase64String = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();

      reader.onload = function (event) {
        const fileContent = event.target.result;
        const base64String = btoa(fileContent);
        resolve(base64String);
      };

      reader.onerror = function (event) {
        reject(event.target.error);
      };

      reader.readAsBinaryString(file);
    });
  };