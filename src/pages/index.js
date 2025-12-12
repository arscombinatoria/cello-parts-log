import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './index.module.css';

const cards = [
  { label: '弦', to: '/strings' },
  { label: '駒', to: '/bridges' },
  { label: 'ペグ', to: '/pegs' },
  { label: '指板', to: '/fingerboards' },
  { label: 'エンドピン', to: '/endpins' },
  { label: 'テールピース', to: '/tailpieces' },
  { label: 'ナット', to: '/nuts' },
  { label: 'サドル', to: '/saddles' },
  { label: '魂柱', to: '/soundposts' },
  { label: 'テールコード', to: '/tailguts' },
  { label: '弦メーカー一覧', to: '/strings/manufacturers' },
];

function HomepageHeader() {
  return (
    <header className={styles.heroBanner}>
      <div className="container">
        <h1 className="hero__title">Cello Parts Log</h1>
        <p className="hero__subtitle">
          チェロのパーツ交換・調整時に気付いたことを整理するための備忘録です。
        </p>
        <p>客観的な仕様と主観的な体感を分けて記録し、再検証しやすい形を目指します。</p>
      </div>
    </header>
  );
}

function CardGrid() {
  return (
    <div className={styles.grid}>
      {cards.map((card) => (
        <Link key={card.to} className={styles.card} to={card.to}>
          {card.label}
        </Link>
      ))}
    </div>
  );
}

export default function Home() {
  return (
    <Layout title="Cello Parts Log" description="チェロパーツ交換のメモ">
      <HomepageHeader />
      <main className="container">
        <CardGrid />
      </main>
    </Layout>
  );
}
