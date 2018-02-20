import presentable, { defaultView } from 'presentable'
import PropTypes from 'prop-types'
import React, { Component } from 'react'
import ReactDom from 'react-dom'

class MyView extends Component {
  render() {
    let { props: { profile: { name, country }}} = this.props.viewModel
    return <>
      <span className="name">{name}</span>
      <span className="country">{country}</span>
    </>
  }
}

@presentable
@defaultView(MyView)
class MyViewModel extends React.Component<*> {
  static contextTypes = {
    testA: PropTypes.string,
    testB: PropTypes.object
  }

  props = {
    profile: { name: 'foo', country: 'bar' }
  }

  arrowMethod = () => {}

  normalMethod() {}
}

ReactDom.render(
  <MyViewModel view={MyView}/>,
  document.getElementById('app')
)
