import re

with open('travelhawk_pitch.html', 'r') as f:
    content = f.read()

# Custom CSS changes
content = content.replace('background-color: #020617;', 'background-color: #f8fafc;')
content = content.replace('color: white;', 'color: #0f172a;')
content = content.replace('background: rgba(30, 41, 59, 0.7);', 'background: rgba(255, 255, 255, 0.8);')
content = content.replace('border: 1px solid rgba(255, 255, 255, 0.1);', 'border: 1px solid rgba(0, 0, 0, 0.05);\n            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.1);')
content = content.replace('from-sky-900 via-slate-950 to-slate-950', 'from-[#002845]/10 via-slate-50 to-slate-50')
content = content.replace('from-sky-400 to-indigo-500', 'from-[#002845] to-[#A12328]')

# Tailwind Class Replacements List
# We use a temporary prefix to avoid overlapping replacement issues!
replacements = {
    'drop-shadow-[0_0_15px_rgba(56,189,248,0.3)]': '',
    'shadow-[0_0_10px_rgba(99,102,241,0.8)]': 'shadow-[0_0_15px_rgba(79,70,229,0.5)]',
    'shadow-[0_0_30px_rgba(56,189,248,0.1)]': 'shadow-[0_0_30px_rgba(0,0,0,0.1)]',
    'mix-blend-luminosity': 'mix-blend-multiply opacity-10',
    
    'border-emerald-500/50': 'border-emerald-300',
    'border-emerald-500/30': 'border-emerald-200',
    'bg-emerald-500/20': 'bg-emerald-100',
    'border-sky-500/50': 'border-[#002845]/30',
    'border-sky-500/30': 'border-[#002845]/20',
    'border-sky-500/20': 'border-[#002845]/10',
    'bg-indigo-500/20': 'bg-indigo-100',
    'bg-sky-500/20': 'bg-[#002845]/10',
    'bg-sky-500/10': 'bg-[#002845]/5',
    'bg-rose-500/20': 'bg-[#A12328]/10',
    'bg-slate-800/80': 'bg-white/90',
    'bg-sky-600/90': 'bg-[#002845]/90',
    
    'hover:bg-slate-700': 'hover:bg-slate-100',
    'hover:bg-sky-500': 'hover:bg-[#002845]/80',
    
    'border-slate-700/50': 'border-slate-200',
    'border-slate-700': 'border-slate-200',
    'border-slate-600': 'border-slate-300',
    'border-sky-400': 'border-[#002845]',
    'border-indigo-400': 'border-indigo-600',
    'border-l-sky-400': 'border-l-[#002845]',
    
    'text-slate-200': 'text-slate-800',
    'text-slate-300': 'text-slate-600',
    'text-slate-400': 'text-slate-500',
    'text-slate-500': 'text-slate-400',
    'text-white': 'text-slate-900',
    
    'text-sky-400': 'text-[#002845]',
    'text-sky-300': 'text-[#002845]',
    'text-sky-100': 'text-[#002845]',
    'text-rose-400': 'text-[#A12328]',
    
    'text-emerald-400': 'text-emerald-700',
    'text-emerald-500': 'text-emerald-600',
    'text-indigo-400': 'text-indigo-700',
    'text-indigo-300': 'text-indigo-800',
    'text-orange-400': 'text-orange-600',
    
    'bg-slate-800': 'bg-white',
    'bg-slate-950': 'bg-slate-50',
    'bg-indigo-500': 'bg-indigo-600',
    
    'from-sky-400': 'from-[#002845]',
    'to-indigo-500': 'to-[#A12328]',
}

# Apply replacements with a TEMP prefix
for old, new in replacements.items():
    content = content.replace(old, f'__TEMP__{new}')

# Remove the TEMP prefix
content = content.replace('__TEMP__', '')

# Further fine-tuning
content = content.replace('from-[#002845]/10 via-slate-50 to-slate-50', 'from-slate-200 via-slate-50 to-slate-50')

with open('travelhawk_pitch.html', 'w') as f:
    f.write(content)
print("Theme updated successfully!")
