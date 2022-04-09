import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom';
import {Navbar} from '../components/navbar/Navbar';
import {AuthProvider} from '../context/AuthProvider';
import {
  Home,
  Stats,
  Configuration,
  Events,
  Camera
} from '../pages';


export const AppRouter = () => {
  return (
    
    <AuthProvider>
      <Router>
        <Routes>
            <Route path="/" element={ <Home /> } />
            <Route path="/stats" element={ <Stats /> } />
            <Route path="/configuration" element={ <Configuration /> } />
            <Route path="/events" element={ <Events /> } />
            <Route path="/camera" element={ <Camera /> } />
        </Routes>
        <Navbar />
      </Router>
    </AuthProvider>

  )
}
