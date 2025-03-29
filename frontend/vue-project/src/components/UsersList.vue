<template>
    <div class="users-list">
      <div class="header">
        <h2>Список пользователей</h2>
        <button @click="$emit('refresh')" :disabled="loading">
          ⟳ Обновить
        </button>
      </div>
  
      <div v-if="loading" class="loading">Загрузка...</div>
      
      <div v-else class="users-container">
        <div v-for="user in users" :key="user.id" class="user-card">
          <div class="user-header">
            <span class="address">{{ user.address }}</span>
            <span class="id">#{{ user.id }}</span>
          </div>
          
          <div class="user-stats">
            <div class="stat-item">
              <span class="label">Balance:</span>
              <span class="value">{{ user.balance }} TRX</span>
            </div>
            <div class="stat-item">
              <span class="label">Bandwidth:</span>
              <span class="value">{{ user.bandwidth }}</span>
            </div>
            <div class="stat-item">
              <span class="label">Energy:</span>
              <span class="value">{{ user.energy }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      users: {
        type: Array,
        required: true
      },
      loading: {
        type: Boolean,
        default: false
      }
    }
  }
  </script>
  
  <style scoped>
  .users-list {
    margin-top: 2rem;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
  }
  
  .user-card {
    background: var(--bg-200);
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }
  
  .user-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  .address {
    font-family: monospace;
    font-size: 0.9rem;
    color: var(--primary-300);
  }
  
  .id {
    font-size: 0.8rem;
    color: var(--text-200);
    opacity: 0.7;
  }
  
  .user-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
  }
  
  .stat-item {
    background: var(--bg-300);
    padding: 1rem;
    border-radius: 6px;
    text-align: center;
  }
  
  .label {
    font-size: 0.8rem;
    color: var(--text-200);
    opacity: 0.8;
    display: block;
    margin-bottom: 0.3rem;
  }
  
  .value {
    font-weight: 600;
    color: var(--accent-200);
  }
  
  .loading {
    text-align: center;
    padding: 2rem;
    color: var(--text-200);
    opacity: 0.7;
  }
  
  button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
  </style>