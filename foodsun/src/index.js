import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import {BrowserRouter, Switch, Route} from 'react-router-dom';

ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path='/' exact component={App}/>
    </Switch>
  </BrowserRouter>,
  document.querySelector('#root')
);

