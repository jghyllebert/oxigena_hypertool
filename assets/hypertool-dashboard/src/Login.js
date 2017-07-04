import React from 'react';


class Login extends React.Component {
  constructor() {
    super();

    this.handleLogin = this.handleLogin.bind(this);
  }

  handleLogin(event) {
    event.preventDefault();

  }


  render() {
    <form className="login-form" onSubmit={(e) => this.handleLogin(e)}>
      <input ref={(input) => this.username = input} type="text" placeholder="Username" required />
      <input ref={(input) => this.password = input} type="password" placeholder="password" required />
      <button>Log in</button>
    </form>

    }
}
