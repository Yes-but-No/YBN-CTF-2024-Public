import React from 'react';

interface CrossIconProps {
  className?: string;
}

const CrossIcon: React.FC<CrossIconProps> = ({ className }) => (
  <svg
    id="Layer_1"
    data-name="Layer 1"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 122.88 122.88"
    className={className}
  >
    <defs>
      <style>
        {`.cls-1 { fill: #ff4141; fill-rule: evenodd; }`}
      </style>
    </defs>
    <title>cross</title>
    <path
      className="cls-1"
      d="M6,6H6a20.53,20.53,0,0,1,29,0l26.5,26.49L87.93,6a20.54,20.54,0,0,1,29,0h0a20.53,20.53,0,0,1,0,29L90.41,61.44,116.9,87.93a20.54,20.54,0,0,1,0,29h0a20.54,20.54,0,0,1-29,0L61.44,90.41,35,116.9a20.54,20.54,0,0,1-29,0H6a20.54,20.54,0,0,1,0-29L32.47,61.44,6,34.94A20.53,20.53,0,0,1,6,6Z"
    />
  </svg>
);

export default CrossIcon;
