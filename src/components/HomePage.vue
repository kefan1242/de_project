<template>
  <div class="home-page">
    <header class="header">
      <h1>数据集探索</h1>
      <p>选择一个数据集开始探索吧！</p>
    </header>
    <div class="card-container">
      <div class="card" @click="navigateTo('/douban')">
        <div class="image-wrapper">
          <img src="/images/douban.jpg" alt="豆瓣影评" />
        </div>
        <div class="content">
          <h2>豆瓣影评</h2>
          <p>28部电影，10万条影评，深度解析。</p>
        </div>
      </div>
      <div class="card" @click="navigateTo('/rottenTomatoes')">
        <div class="image-wrapper">
          <img src="/images/rottenTomatoes.jpg" alt="烂番茄影评" />
        </div>
        <div class="content">
          <h2>烂番茄影评</h2>
          <p>100万条影评，广泛覆盖。</p>
        </div>
      </div>
      <div class="card" @click="navigateTo('/amazonBooks')">
        <div class="image-wrapper">
          <img src="/images/amazonBooks.jpg" alt="Amazon书评" />
        </div>
        <div class="content">
          <h2>Amazon书评</h2>
          <p>1500本书，16万条评论，深入挖掘。</p>
        </div>
      </div>
      <div class="card" @click="navigateTo('/wine')">
        <div class="image-wrapper">
          <img src="/images/wine.jpg" alt="Wine Enthusiast酒评" />
        </div>
        <div class="content">
          <h2>酒评数据</h2>
          <p>15万条酒评，品味独特风味。</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  methods: {
    navigateTo(path) {
      this.$router.push(path);
    },
  },
};
</script>

<style>
/* 页面整体样式 */
.home-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: linear-gradient(to bottom, #e8f5e9, #e0f7fa);
  min-height: 100vh;
}

/* 头部样式 */
.header {
  text-align: center;
  margin-bottom: 20px; /* 减少文字与卡片的间距 */
}

.header h1 {
  font-size: 36px;
  font-weight: bold;
  color: #2e7d32;
  margin-bottom: 8px; /* 减少标题与描述文字的间距 */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

.header p {
  font-size: 18px;
  color: #455a64;
}

/* 卡片容器样式 */
.card-container {
  display: grid;
  grid-template-columns: 1fr 1fr; /* 两列布局 */
  gap: 20px; /* 卡片间距 */
  width: 100%;
  max-width: 800px;
  padding: 10px; /* 缩小卡片容器与文字的间距 */
}

/* 卡片样式 */
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

/* 图片样式 */
.image-wrapper {
  width: 100%;
  height: 140px; /* 调整图片容器高度 */
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

/* 卡片内容样式 */
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
</style>
