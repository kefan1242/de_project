<template>
  <div class="page">
    <div class="image-gallery">
      <img src="wine1.jpg" alt="Wine Image 1" />
      <img src="wine2.jpg" alt="Wine Image 2" />
      <img src="wine3.jpg" alt="Wine Image 3" />
      <img src="wine4.jpg" alt="Wine Image 4" />
    </div>
    <div class="chat-container">
      <h2>Wine Enthusiast Chat Box</h2>
      <div class="messages">
        <div
          v-for="(message, index) in messages"
          :key="index"
          :class="['message', message.sender]"
        >
          <p>{{ message.text }}</p>
        </div>
      </div>
      <div class="input-box">
        <input
          type="text"
          v-model="userInput"
          placeholder="Enter your message..."
          @keyup.enter="sendMessage"
        />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
    <!-- 固定左下角的返回按钮 -->
    <button class="back-button" @click="goBack">返回主界面</button>
  </div>
</template>

<script>
export default {
  name: "WinePage",
  data() {
    return {
      userInput: "",
      messages: [
        { text: "欢迎来到 Wine Enthusiast 页面，请问有什么可以帮助您？", sender: "bot" },
      ],
    };
  },
  methods: {
    goBack() {
      this.$router.push("/");
    },
    async sendMessage() {
      if (this.userInput.trim() !== "") {
        this.messages.push({ text: this.userInput, sender: "user" });
        const question = this.userInput;
        this.userInput = "";

        try {
          const response = await fetch("http://127.0.0.1:8000/gpt/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ question }),
          });

          if (!response.ok) {
            throw new Error("网络响应错误");
          }

          const data = await response.json();
          if (data.success) {
            this.messages.push({
              text: data.data,
              sender: "bot",
            });
          } else {
            this.messages.push({
              text: "后端返回错误，请稍后再试。",
              sender: "bot",
            });
          }
        } catch (error) {
          this.messages.push({
            text: "无法连接到后端服务，请检查网络或后端状态。",
            sender: "bot",
          });
        }
      }
    },
  },
};
</script>

<style>
/* 样式与 DoubanPage 相同 */
.page {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  height: 100vh;
  padding: 20px;
  background: linear-gradient(to right, #fef9f9, #fff5f3);
  position: relative;
}

.image-gallery {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: 50%;
}

.image-gallery img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.image-gallery img:hover {
  transform: scale(1.05);
}

.chat-container {
  width: 45%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  border-radius: 12px;
  background: linear-gradient(to bottom, #ffffff, #ffecf0);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.chat-container h2 {
  font-size: 24px;
  margin-bottom: 10px;
  text-align: center;
  color: #b71c1c;
}

.messages {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 15px;
  padding: 15px;
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
}

.message {
  margin: 10px 0;
  padding: 12px;
  border-radius: 8px;
  font-size: 14px;
  line-height: 1.5;
}

.message.user {
  background-color: #ffab91;
  text-align: right;
  color: #b71c1c;
}

.message.bot {
  background-color: #ffcccb;
  text-align: left;
  color: #d50000;
}

.input-box {
  display: flex;
  gap: 10px;
  align-items: center;
}

input[type="text"] {
  flex: 1;
  padding: 12px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

button {
  padding: 12px 20px;
  font-size: 14px;
  font-weight: bold;
  background-color: #b71c1c;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: #e57373;
  transform: translateY(-2px);
}

/* 固定左下角的返回按钮 */
.back-button {
  position: fixed;
  bottom: 20px;
  left: 20px;
  padding: 10px 20px;
  font-size: 14px;
  background-color: #b71c1c;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.back-button:hover {
  background-color: #d50000;
  transform: translateY(-2px);
}
</style>
