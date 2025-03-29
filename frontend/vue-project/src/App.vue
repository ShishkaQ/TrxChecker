<template>
  <div class="wallet-checker">
    <h1>Проверка TRX кошелька</h1>
    <form @submit.prevent="submitForm">
      <div class="input-group">
        <input
          type="text"
          v-model="walletAddress"
          placeholder="Введите ваш TRX-адрес"
          :disabled="isLoading"
        />
        <button type="submit" :disabled="isLoading || !walletAddress">
          {{ isLoading ? 'Проверка...' : 'Проверить' }}
        </button>
      </div>
      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>
    </form>

    <div class="view-switcher">
      <button 
        @click="switchView('wallet')" 
        :class="{ active: activeView === 'wallet' }"
      >
        Информация о кошельке
      </button>
      <button 
        @click="switchView('users')" 
        :class="{ active: activeView === 'users' }"
      >
        Список пользователей
      </button>
    </div>

    <transition name="wallet-fade">
      <WalletInfo 
        v-if="activeView === 'wallet' && walletData"
        :address="lastCheckedAddress"
        :bandwidth="walletData.bandwidth"
        :energy="walletData.energy"
        :balance="walletData.balance"
        @close="clearData"
      />
    </transition>
    
    <transition name="slide-fade">
      <UsersList 
        v-if="activeView === 'users'"
        :users="users"
        :loading="usersLoading"
        :error="usersError"
        @refresh="fetchUsers"
      />
    </transition>
  </div>
</template>

<script>
import axios from 'axios'
import WalletInfo from './components/WalletInfo.vue'
import UsersList from './components/UsersList.vue'

export default {
  components: {
    WalletInfo,
    UsersList
  },
  data() {
    return {
      walletAddress: '',
      lastCheckedAddress: '',
      errorMessage: '',
      isLoading: false,
      walletData: null,
      activeView: 'wallet',
      users: [],
      usersLoading: false,
      usersError: null
    }
  },
  methods: {
    validateAddress(address) {
      const trxRegex = /^T[A-Za-z1-9]{33}$/
      return trxRegex.test(address)
    },
    
    switchView(view) {
      this.activeView = view
      if (view === 'users' && this.users.length === 0) {
        this.fetchUsers()
      }
    },
    
    async submitForm() {
      this.errorMessage = ''
      this.walletData = null
      
      if (!this.walletAddress) {
        this.errorMessage = 'Пожалуйста, введите адрес кошелька'
        return
      }
      
      if (!this.validateAddress(this.walletAddress)) {
        this.errorMessage = 'Неверный формат TRX-адреса'
        return
      }
      
      try {
        this.isLoading = true
        this.lastCheckedAddress = this.walletAddress
        this.activeView = 'wallet'
        
        const response = await axios.post("http://localhost:8000/address-info/", {
          "address": this.lastCheckedAddress
        });

        this.walletData = response.data
        this.walletAddress = ''
      } catch (error) {
        this.errorMessage = 'Ошибка при проверке адреса'
      } finally {
        this.isLoading = false
      }
    },
    
    clearData() {
      this.walletData = null
      this.lastCheckedAddress = ''
    },
    
    async fetchUsers() {
      try {
        this.usersLoading = true
        this.usersError = null
        
        const response = await axios.get('http://localhost:8000/users-info/')
        this.users = response.data.map(user => ({
          ...user,
          balance: Number(user.balance).toFixed(6)
        }))
      } catch (error) {
        this.usersError = 'Ошибка загрузки списка пользователей'
        console.error('Ошибка:', error)
      } finally {
        this.usersLoading = false
      }
    }
  }
}
</script>

<style scoped>
.wallet-checker {
  max-width: 800px;
  margin: 4rem auto 2rem;
  padding: 2rem;
  text-align: center;
  background: var(--bg-300);
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h1 {
  color: var(--primary-300);
  margin-bottom: 2rem;
  font-weight: 600;
}

.input-group {
  display: flex;
  gap: 10px;
  margin-bottom: 1rem;
}

input {
  flex: 1;
  padding: 14px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  background: var(--bg-200);
  color: var(--text-200);
  transition: all 0.3s ease;
}

input:focus {
  outline: 2px solid var(--primary-300);
  outline-offset: 2px;
}

button {
  padding: 14px 28px;
  background-color: var(--primary-200);
  color: var(--accent-200);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 500;
}

.error-message {
  color: #ff6b6b;
  margin: 1rem 0;
  font-size: 14px;
  padding: 8px;
  background: rgba(255, 107, 107, 0.1);
  border-radius: 6px;
}

.view-switcher {
  margin: 1.5rem 0;
  display: flex;
  gap: 1rem;
  justify-content: center;
}

/* Анимации */
.wallet-fade-enter-active,
.wallet-fade-leave-active {
  transition: all 0.3s ease;
}
.wallet-fade-enter-from,
.wallet-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}
.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(20px);
  opacity: 0;
}

@media (max-width: 640px) {
  .wallet-checker {
    margin: 2rem 1rem;
    padding: 1.5rem;
  }
  
  .input-group {
    flex-direction: column;
  }
  
  button {
    width: 100%;
  }
}
</style>