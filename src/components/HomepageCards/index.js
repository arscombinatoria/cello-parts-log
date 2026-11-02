import React from 'react';
import Link from '@docusaurus/Link';
import styles from './index.module.css';

const cards = [
  {name: '弦', description: '音色・張力・メーカーを比較', to: '/strings'},
  {name: '駒', description: '材質・形状と調整の違い', to: '/bridges'},
  {name: 'ペグ', description: '調弦の操作性と方式を比較', to: '/pegs'},
  {name: '指板', description: '材質・形状と弾きやすさ', to: '/fingerboards'},
  {name: 'エンドピン', description: '材質・重量と響きの関係', to: '/endpins'},
  {name: 'テールピース', description: '材質・重量・アジャスター', to: '/tailpieces'},
  {name: 'ナット', description: '弦高・溝の形状と演奏性', to: '/nuts'},
  {name: 'サドル', description: '構造・材質と保守上の注意', to: '/saddles'},
  {name: '魂柱', description: '配置・調整と音響への影響', to: '/soundposts'},
  {name: 'テールコード', description: '材質・長さと響きの関係', to: '/tailguts'},
  {name: '弓', description: '材質・重量・選び方', to: '/bows'},
  {name: '松脂', description: '摩擦特性と銘柄の比較', to: '/rosin'},
  {name: 'ケース', description: '保護性能・重量・メーカー', to: '/cases'},
];

export default function HomepageCards() {
  return (
    <ul className={styles.grid}>
      {cards.map(({name, description, to}) => (
        <li key={to} className={styles.item}>
          <Link className={styles.card} to={to}>
            <span className={styles.name}>{name}</span>
            <span className={styles.description}>{description}</span>
          </Link>
        </li>
      ))}
    </ul>
  );
}
