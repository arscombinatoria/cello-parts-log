import Link from 'next/link';

const links = [
  { href: '/strings', label: '弦' },
  { href: '/bridges', label: '駒' },
  { href: '/pegs', label: 'ペグ' },
  { href: '/fingerboards', label: '指板' },
  { href: '/endpins', label: 'エンドピン' },
  { href: '/tailpieces', label: 'テールピース' },
  { href: '/nuts', label: 'ナット' },
  { href: '/saddles', label: 'サドル' },
  { href: '/soundposts', label: '魂柱' },
  { href: '/tailguts', label: 'テールコード' },
  { href: '/strings/manufacturers', label: '弦メーカー一覧' },
];

export default function Home() {
  return (
    <main>
      <h1>チェロのパーツ交換についての備忘録</h1>
      <p>チェロの各パーツについて、交換や調整の参考になりそうな情報をLLMを使ってWebで調べた内容からまとめています。</p>
      <div className="grid">
        {links.map(link => (
          <Link key={link.href} href={link.href} legacyBehavior>
            <a>{link.label}</a>
          </Link>
        ))}
      </div>
    </main>
  );
}
