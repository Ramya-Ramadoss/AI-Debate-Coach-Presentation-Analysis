import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Mic, History, UserCog, Sparkles } from 'lucide-react';

const Sidebar = () => {
  const navItems = [
    { to: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { to: '/create-debate', label: 'Create Debate', icon: Mic },
    { to: '/my-debates', label: 'My Debates', icon: History },
    { to: '/profile', label: 'My Profile', icon: UserCog },
  ];

  return (
    <aside className="w-64 glass-panel border-r border-white/5 min-h-[calc(100vh-73px)] p-4 flex flex-col justify-between hidden md:flex">
      <div className="space-y-6">
        <div className="px-3 text-xs font-semibold text-purple-400/70 tracking-widest uppercase">
          Navigation
        </div>
        <nav className="space-y-2">
          {navItems.map((item) => {
            const Icon = item.icon;
            return (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) =>
                  `flex items-center gap-3 px-4 py-3 rounded-xl transition duration-200 font-medium text-sm border border-transparent ${
                    isActive
                      ? 'bg-gradient-to-r from-purple-900/50 to-blue-900/20 text-white border-purple-500/30 shadow-inner'
                      : 'text-slate-400 hover:text-white hover:bg-white/5'
                  }`
                }
              >
                <Icon className="w-4 h-4" />
                {item.label}
              </NavLink>
            );
          })}
        </nav>
      </div>

      <div className="glass-panel p-4 rounded-2xl border border-white/5 bg-gradient-to-br from-purple-950/20 to-blue-950/20 shadow-lg relative overflow-hidden">
        <div className="absolute -top-10 -right-10 w-24 h-24 bg-purple-600/10 rounded-full blur-xl"></div>
        <div className="flex items-center gap-2 text-purple-300 font-semibold text-xs mb-2">
          <Sparkles className="w-4 h-4 text-purple-400 animate-pulse" />
          AI Coach Offline
        </div>
        <p className="text-[10px] text-slate-400 leading-relaxed">
          AI argument coaching and logical fallacy analysis will be activated in Week 2.
        </p>
      </div>
    </aside>
  );
};

export default Sidebar;
