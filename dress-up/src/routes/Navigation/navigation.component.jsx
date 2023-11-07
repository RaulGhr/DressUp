import { Fragment } from "react";
import { Outlet, Link } from 'react-router-dom';

import "./navigation.style.scss";

const Navigation = () => {
  return (
    <Fragment>
      <div className="navigation">
        <Link to="/" className="link">
          <h1>DressUp</h1>
        </Link>
      </div>
      <Outlet />
    </Fragment>
  );
};

export default Navigation;
