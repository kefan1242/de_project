<template>
  <div class="home-page">
    <header class="header">
      <h1>Dataset Exploration</h1>
      <p>Select a dataset to start exploring!</p>
      <button class="upload-button" @click="showModal = true">Upload Dataset</button>
    </header>
    <div class="card-container">
      <div class="card" @click="navigateTo('/douban')">
        <div class="image-wrapper">
          <img :src="require('@/assets/d1.png')" alt="Douban Movie Reviews" />
        </div>
        <div class="content">
          <h2>Douban Movie Reviews</h2>
          <p>28 movies, 100,000 reviews, in-depth analysis.</p>
        </div>
      </div>
      <div class="card" @click="navigateTo('/rottenTomatoes')">
        <div class="image-wrapper">
          <img :src="require('@/assets/lanfanqie.png')" alt="Rotten Tomatoes Reviews" />
        </div>
        <div class="content">
          <h2>Rotten Tomatoes Reviews</h2>
          <p>1 million reviews, wide coverage.</p>
        </div>
      </div>
      <div class="card" @click="navigateTo('/amazonBooks')">
        <div class="image-wrapper">
          <img :src="require('@/assets/book.png')" alt="Amazon Book Reviews" />
        </div>
        <div class="content">
          <h2>Amazon Book Reviews</h2>
          <p>1,500 books, 160,000 reviews, in-depth exploration.</p>
        </div>
      </div>
      <div class="card" @click="navigateTo('/wine')">
        <div class="image-wrapper">
          <img :src="require('@/assets/wine.png')" alt="Wine Enthusiast Reviews" />
        </div>
        <div class="content">
          <h2>Wine Reviews</h2>
          <p>150,000 wine reviews, discover unique flavors.</p>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <h2 v-if="isLogin">Login</h2>
        <h2 v-else>Register</h2>
        <form @submit.prevent="handleSubmit">
          <div v-if="isLogin">
            <input type="file" @change="handleFileUpload" class="form-input" />
            <input
              type="email"
              v-model="loginForm.email"
              placeholder="Email"
              class="form-input"
            />
            <input
              type="password"
              v-model="loginForm.password"
              placeholder="Password"
              class="form-input"
            />
            <button type="submit" class="form-button">Login & Upload</button>
            <p class="toggle-text" @click="isLogin = false">Go to Register</p>
          </div>

          <div v-else>
            <input
              type="email"
              v-model="registerForm.email"
              placeholder="Email"
              class="form-input"
            />
            <input
              type="text"
              v-model="registerForm.username"
              placeholder="Username"
              class="form-input"
            />
            <input
              type="password"
              v-model="registerForm.password"
              placeholder="Password"
              class="form-input"
            />
            <button type="submit" class="form-button">Register</button>
            <p class="toggle-text" @click="isLogin = true">Go to Login</p>
          </div>
        </form>
        <button class="close-button" @click="closeModal">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      showModal: false,
      isLogin: true,
      loginForm: {
        email: "",
        password: "",
      },
      registerForm: {
        email: "",
        username: "",
        password: "",
      },
      selectedFile: null,
    };
  },
  methods: {
    navigateTo(path) {
      this.$router.push(path);
    },
    closeModal() {
      this.showModal = false;
    },
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
      console.log("Uploaded file:", this.selectedFile);
    },
    async handleSubmit() {
      if (this.isLogin) {
        // Login and upload file
        const formData = new FormData();
        formData.append("email", this.loginForm.email);
        formData.append("password", this.loginForm.password);
        formData.append("file", this.selectedFile);

        try {
          const response = await fetch('http://127.0.0.1:8000/api/login', {
            method: 'POST',
            body: formData
          });
          if (!response.ok) {
            throw new Error("Login failed");
          }
          const data = await response.json();
          console.log("Login successful:", data);
        } catch (error) {
          console.error("Login failed:", error);
        }
      } else {
        // Register
        const formData = new FormData();
        formData.append("email", this.registerForm.email);
        formData.append("username", this.registerForm.username);
        formData.append("password", this.registerForm.password);

        try {
          const response = await fetch('http://127.0.0.1:8000/api/register', {
            method: 'POST',
            body: formData
          });
          if (!response.ok) {
            throw new Error("Registration failed");
          }
          const data = await response.json();
          console.log("Registration successful:", data);
        } catch (error) {
          console.error("Registration failed:", error);
        }
      }
      this.closeModal();
    },
  },
};
</script>

<style>
/* Overall page style */
.home-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: linear-gradient(to bottom, #e8f5e9, #e0f7fa);
  min-height: 100vh;
}

/* Header style */
.header {
  text-align: center;
  margin-bottom: 20px;
  position: relative;
  width: 100%;
}

.upload-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px 20px;
  background-color: #42a5f5;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.upload-button:hover {
  background-color: #1e88e5;
}

/* Card container style */
.card-container {
  display: grid;
  grid-template-columns: 1fr 1fr; /* Two-column layout */
  gap: 20px; /* Card spacing */
  width: 100%;
  max-width: 800px;
  padding: 10px; /* Reduce spacing between card container and text */
}

/* Card style */
.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border-radius: 12px;
  background: linear-gradient(to bottom right, #ffffff, #f1f8e9);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
}

/* Image style */
.image-wrapper {
  width: 100%;
  height: 140px; /* Adjust image container height */
  overflow: hidden;
  background-color: #e0f2f1;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.card:hover .image-wrapper img {
  transform: scale(1.1);
}

/* Card content style */
.content {
  padding: 10px 15px;
}

.content h2 {
  font-size: 18px;
  color: #2e7d32;
  margin-bottom: 6px;
}

.content p {
  font-size: 14px;
  color: #607d8b;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  backdrop-filter: blur(5px); /* Add blur effect */
}

.modal {
  background: white;
  padding: 30px;
  border-radius: 16px;
  width: 400px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  position: relative;
  text-align: center;
}

.form-input {
  width: 100%;
  padding: 15px;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
}

.form-button {
  width: 100%;
  padding: 15px;
  background-color: #42a5f5;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.form-button:hover {
  background-color: #1e88e5;
}

.toggle-text {
  text-align: center;
  color: #42a5f5;
  cursor: pointer;
  margin-top: 15px;
  font-size: 14px;
}

.close-button {
  margin-top: 20px;
  padding: 10px;
  background-color: #ef5350;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  width: 100%;
  font-size: 16px;
}

.close-button:hover {
  background-color: #d32f2f;
}
</style>
