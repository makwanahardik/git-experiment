webpackJsonp([12,13],{2388:function(e,t,n){"use strict";(function(e){Object.defineProperty(t,"__esModule",{value:!0});var i=n(642),s=n(342),c=n(1724),o=n(1684),r=n(159),a=function(e){return{isFetchingMe:c.a.State.isFetchingMe(e)}},h=n.i(o.a)("fetchMe","fetchConnectEnrollment","fetchApplications"),l=n.i(i.b)(a,h)(e.createClass({displayName:"me/container",propTypes:{isFetchingMe:e.PropTypes.bool.isRequired,fetchMe:e.PropTypes.func.isRequired,fetchConnectEnrollment:e.PropTypes.func.isRequired,fetchApplications:e.PropTypes.func.isRequired},getInitialState:function(){return{hasFetched:!1}},componentWillMount:function(){this.props.fetchMe(),this.props.fetchConnectEnrollment(),this.props.fetchApplications(),this._setHasFetched(!1)},componentWillReceiveProps:function(e){this.state.hasFetched||e.isFetchingMe||this._setHasFetched(!0)},_setHasFetched:function(e){this.setState({hasFetched:e})},render:function(){var t=this.state.hasFetched;return e.createElement(s.b,{isBusy:!t,documentTitle:n.i(r.b)("Home"),isLargePrimaryNav:!0},e.createElement(s.b.Header,{title:n.i(r.b)("Home")}),e.createElement(s.b.Body,null,t?this.props.children:null))}}));t.default=l}).call(t,n(0))}});